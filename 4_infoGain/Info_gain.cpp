#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <cmath>
using namespace std;

// Function to calculate information entropy
double calculateInformationEntropy(int positive, int negative)
{
    double total = positive + negative;
    double entropy = 0.0;

    if (total > 0)
    {
        double positiveProbability = positive / total;
        double negativeProbability = negative / total;

        if (positiveProbability > 0)
        {
            entropy -= positiveProbability * log2(positiveProbability);
        }

        if (negativeProbability > 0)
        {
            entropy -= negativeProbability * log2(negativeProbability);
        }
    }

    return entropy;
}

// Function to compute information gain
double computeInformationGain(map<string, int> &parentCounts, map<string, map<string, int>> &childCounts)
{
    double positiveParent = parentCounts["Yes"];
    double negativeParent = parentCounts["No"];
    double totalParent = positiveParent + negativeParent;

    double parentEntropy = calculateInformationEntropy(positiveParent, negativeParent);
    cout << "Total Entropy: " << parentEntropy << "\n";

    double childEntropy = 0;

    for (auto it = childCounts.begin(); it != childCounts.end(); ++it)
    {
        string childName = it->first;
        double positiveChild = it->second["Yes"];
        double negativeChild = it->second["No"];
        double totalChild = positiveChild + negativeChild;

        double childEntropyPart = calculateInformationEntropy(positiveChild, negativeChild);

        childEntropy += (totalChild / totalParent) * childEntropyPart;
    }


    double informationGain = parentEntropy - childEntropy;
    cout << "Information Gain: " << informationGain << "\n";

    return informationGain;
}

int main()
{
    ifstream inputFile("Input.csv");

    string line, Day, Direction, WaterLevel, ToFill, value;
    map<string, int> parentCounts;
    map<string, map<string, int>> childCounts;

    if (!inputFile.is_open())
    {
        cerr << "Error opening input file." << endl;
        return -1;
    }

    int lineIndex = 0;
    string childName;
    int choice;

    while (getline(inputFile, line))
    {
        stringstream lineStream(line);
        getline(lineStream, Day, ',');
        getline(lineStream, Direction, ',');
        getline(lineStream, WaterLevel, ',');
        getline(lineStream, ToFill, ',');
        getline(lineStream, value, ',');

        if (lineIndex == 0)
        {
            lineIndex++;
            cout << "Enter Child Column Number: ";
            cin >> choice;
            continue;
        }

        switch (choice)
        {
        case 1:
            childName = Day;
            break;

        case 2:
            childName = Direction;
            break;

        case 3:
            childName = WaterLevel;
            break;

        case 4:
            childName = value;
            break;

        default:
            childName = WaterLevel;
            break;
        }

        parentCounts[ToFill]++;
        childCounts[childName][ToFill]++;
    }

    double informationGain = computeInformationGain(parentCounts, childCounts);

    return 0;
}
