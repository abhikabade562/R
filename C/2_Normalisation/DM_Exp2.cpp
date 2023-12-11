#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

void findMinMax(const vector<double>& data, double& minValue, double& maxValue) {
    minValue = *min_element(data.begin(), data.end());
    maxValue = *max_element(data.begin(), data.end());
}

void applyMinMaxNormalization(const vector<double>& data, ofstream& outputFile, double oldMin, double oldMax, double newMin, double newMax) {
    outputFile << "Original Data,Normalized Data\n";

    for (double value : data) {
        double normalizedValue = (((value - oldMin) / (oldMax - oldMin)) * (newMax - newMin)) + newMin;
        outputFile << value << "," << normalizedValue << "\n";
    }
}

void applyZScoreNormalization(const vector<double>& data, ofstream& outputFile) {
    double sum = 0.0, squareSum = 0.0;
    int count = data.size();

    for (double value : data) {
        sum += value;
        squareSum += (value * value);
    }

    double mean = sum / count;
    double variance = (squareSum / count) - (mean * mean);
    double standardDeviation = sqrt(variance);

    outputFile << "Original Data,Normalized Data\n";

    for (double value : data) {
        double normalizedValue = (value - mean) / standardDeviation;
        outputFile << value << "," << normalizedValue << "\n";
    }
}

int main() {
    vector<double> inputData;
    double newMinValue, newMaxValue;
    int choice;

    ifstream inputFileMinMax("MINMAX_input.csv");
    ifstream inputFileZScore("MINMAX_input.csv");
    ofstream outputFileMinMax("MINMAX_output.csv", ios::app);
    ofstream outputFileZScore("Z_Score_output.csv", ios::app);

    if (!inputFileMinMax || !outputFileMinMax || !inputFileZScore || !outputFileZScore) {
        cerr << "Error opening files. Please try again." << endl;
        return 1;
    }

    double value;
   
    cout << "Select one choice :\n1. Min-Max Normalization\t2. Z-Score Normalization\nEnter your choice: ";
    cin >> choice;

    switch (choice) {
        case 1: // Min-Max Normalization
            while (inputFileMinMax >> value) {
                inputData.push_back(value);
            }
            cout << "Enter new minimum value: ";
            cin >> newMinValue;
            cout << "Enter new maximum value: ";
            cin >> newMaxValue;
            double minValue, maxValue;
            findMinMax(inputData, minValue, maxValue);
            applyMinMaxNormalization(inputData, outputFileMinMax, minValue, maxValue, newMinValue, newMaxValue);
            cout<<"Check MINMAX_output.csv file for upadated normalised MINMAX data"<<endl;
            break;

        case 2: // Z-Score Normalization
            while (inputFileZScore >> value) {
                inputData.push_back(value);
            }
            applyZScoreNormalization(inputData, outputFileZScore);
            cout<<"Check Z_Score_output.csv file for upadated normalised ZScore data"<<endl;
            break;

        default:
            cerr << "Invalid choice" << endl;
    }

    return 0;
}
