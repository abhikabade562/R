#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

// Function to calculate the median of a vector
float calculateMedian(vector<int> data)
{
    int size = data.size();
    if (size % 2 == 1)
        return data[size / 2];
    else
        return (data[(size / 2) - 1] + data[size / 2]) / 2.0;
}

// Function to calculate the first quartile (Q1)
float calculateFirstQuartile(vector<int> data)
{
    int n = data.size();
    vector<int> first;

    for (int i = 0; i < n / 2; i++)
    {
        first.push_back(data[i]);
    }
    return calculateMedian(first);
}

// Function to calculate the third quartile (Q3)
float calculateThirdQuartile(vector<int> data)
{
    int n = data.size();
    vector<int> last;
    if (n % 2 == 0)
    {
        for (int i = n / 2; i < n; i++)
        {
            last.push_back(data[i]);
        }
    }
    else
    {
        for (int i = n / 2 + 1; i < n; i++)
        {
            last.push_back(data[i]);
        }
    }
    return calculateMedian(last);
}

int main()
{
    ifstream inputFile("Input_File.csv");
    if (!inputFile.is_open())
    {
        cout << "Error: Unable to open the input file." << endl;
        exit(0);
    }

    ofstream outputFile("Output_File.csv");

    int i = 0;
    string line, mark;
    vector<int> data;

    // Read data from the input file
    while (getline(inputFile, line))
    {
        if (i == 0)
        {
            i++;
            continue;
        }
        stringstream lineStream(line);

        getline(lineStream, mark, ',');
        int x = stoi(mark);
        data.push_back(x);
    }

    int n = data.size();
    sort(data.begin(), data.end());

    // Write results to the output file and console
    outputFile << "Minimum value: "
        << "," << data[0] << "\n";
    outputFile << "First Quartile (Q1) value: "
        << "," << calculateFirstQuartile(data) << "\n";
    outputFile << "Median value: "
        << "," << calculateMedian(data) << "\n";
    outputFile << "Third Quartile (Q3) value: "
        << "," << calculateThirdQuartile(data) << "\n";
    outputFile << "Maximum value: "
        << "," << data[n - 1] << "\n";

    cout << "The minimum value is " << data[0] << endl;
    cout << "The First Quartile (Q1) is " << calculateFirstQuartile(data) << endl;
    cout << "The median is " << calculateMedian(data) << endl;
    cout << "The Third Quartile (Q3) is " << calculateThirdQuartile(data) << endl;
    cout << "The maximum value is " << data[n - 1] << endl;

    return 0;
}
