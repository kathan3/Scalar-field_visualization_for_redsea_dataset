#ifndef VTK_FILEREADER_H
#define VTK_FILEREADER_H

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_map>
#include <glm/glm.hpp>

class VTKFileReader {
public:
    bool readFile(const std::string& filename);

    glm::ivec3 dimensions;
    glm::vec3 spacing;
    glm::vec3 origin;
    std::unordered_map<std::string, std::vector<double>> fieldData;
private:
    void parseDimensions(std::ifstream& file);
    void parseSpacing(std::ifstream& file);
    void parseOrigin(std::ifstream& file);
    void parsePointData(std::ifstream& file, int numPoints);
    void parseFieldData(std::ifstream& file, int numFields);

};

bool VTKFileReader::readFile(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return false;
    }

    std::string line;
    // Read header
    for (int i = 0; i < 3; ++i) {
        std::getline(file, line);
        std::cout << line << std::endl; // Print header lines
    }

    // Read dataset type
    std::getline(file, line);
    std::cout << line << std::endl; // Print dataset type

    if (line.find("STRUCTURED_POINTS") != std::string::npos) {
        parseDimensions(file);
        parseSpacing(file);
        parseOrigin(file);

        // Read point data
        std::getline(file, line); // POINT_DATA line
        std::istringstream iss(line);
        std::string keyword;
        int numPoints;
        iss >> keyword >> numPoints;

        // Read field data
        std::getline(file, line); // FIELD line
        iss.clear();
        iss.str(line);
        std::string fieldKeyword;
        int numFields;
        iss >> fieldKeyword >> fieldKeyword >> numFields;
        parseFieldData(file, numFields);
    }

    file.close();
    return true;
}

void VTKFileReader::parseDimensions(std::ifstream& file) {
    std::string line;
    std::getline(file, line);
    std::istringstream iss(line);
    std::string keyword;
    iss >> keyword >> dimensions.x >> dimensions.y >> dimensions.z;
    std::cout << "Dimensions: " << dimensions.x << " " << dimensions.y << " " << dimensions.z << std::endl;
}

void VTKFileReader::parseSpacing(std::ifstream& file) {
    std::string line;
    std::getline(file, line);
    std::istringstream iss(line);
    std::string keyword;
    iss >> keyword >> spacing.x >> spacing.y >> spacing.z;
    std::cout << "Spacing: " << spacing.x << " " << spacing.y << " " << spacing.z << std::endl;
}

void VTKFileReader::parseOrigin(std::ifstream& file) {
    std::string line;
    std::getline(file, line);
    std::istringstream iss(line);
    std::string keyword;
    iss >> keyword >> origin.x >> origin.y >> origin.z;
    std::cout << "Origin: " << origin.x << " " << origin.y << " " << origin.z << std::endl;
}

void VTKFileReader::parseFieldData(std::ifstream& file, int numFields) {
    std::string line;
    for (int i = 0; i < numFields; ++i) {
        std::getline(file, line); // Field name line
        while(line.empty() || line[0] == ' ') {
            std::getline(file, line);
        }
        std::cout << line << "-" << std::endl;
        std::istringstream iss(line);
        std::string fieldName;
        int numComponents, numTuples;
        std::string dataType;
        iss >> fieldName >> numComponents >> numTuples >> dataType;

        std::vector<double> data;
        data.reserve(numTuples);
        for (int j = 0; j < numTuples; ++j) {
            double value;
            file >> value;
            data.push_back(value);
        }
        fieldData[fieldName] = data;
    }

    for (const auto& field : fieldData) {
        std::cout << "Field: " << field.first << " with " << field.second.size() << " values" << std::endl;
    }
}

#endif // VTK_FILEREADER_H