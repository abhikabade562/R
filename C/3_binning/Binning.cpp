#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;

// Equal Frequency Binning
vector<vector<int>> equalFrequencyBinning(vector<int> data, int numBins)
{
  int dataSize = data.size();
  int binSize = dataSize / numBins;
  vector<vector<int>> bins;

  for (int i = 0; i < numBins; i++)
  {
    vector<int> bin;
    for (int j = i * binSize; j < (i + 1) * binSize; j++)
    {
      if (j >= dataSize)
      {
        break;
      }
      bin.push_back(data[j]);
    }
    bins.push_back(bin);
  }
  return bins;
}

// Bin by Mean Binning
vector<vector<int>> binByMeanBinning(vector<int> data, int numBins)
{
  int dataSize = data.size();
  int binSize = dataSize / numBins;

  vector<vector<int>> bins(numBins);

  // Divide input numbers equally into bins
  for (int i = 0; i < numBins; i++)
  {
    for (int j = i * binSize; j < (i + 1) * binSize; j++)
    {
      if (j < dataSize)
      {
        bins[i].push_back(data[j]);
      }
    }
  }

  // Calculate mean for each bin and update values
  for (auto &bin : bins)
  {
    if (!bin.empty())
    {
      int binMean = accumulate(bin.begin(), bin.end(), 0) / bin.size();

      // Update all values in the bin with the mean
      fill(bin.begin(), bin.end(), binMean);
    }
  }

  return bins;
}

// Read data from CSV
vector<int> readCSV(string filename)
{
  ifstream inputFile(filename);
  vector<int> data;
  string line, value;
  while (getline(inputFile, line))
  {
    stringstream ss(line);
    while (getline(ss, value, ','))
    {
      data.push_back(stoi(value));
    }
  }
  inputFile.close();
  return data;
}

// Write binning outputs to CSV
void writeCSV(string filename, vector<vector<int>> bins)
{
  ofstream outputFile(filename);
  for (int i = 0; i < bins.size(); i++)
  {
    outputFile << "Bin " << i + 1 << ",";
    for (int num : bins[i])
    {
      outputFile << num << ",";
    }
    outputFile << "\n";
  }
  outputFile.close();
}

int main()
{
  vector<int> data = readCSV("Input_file.csv");
  int numBins;

  int method;
  cout << "Choose binning method: " << endl;
  cout << "1. Equal Frequency Binning" << endl;
  cout << "2. Bin by Mean Binning" << endl; // Updated option
  cout << "\nEnter method number: ";
  cin >> method;
  cout << "\nEnter number of bins: ";
  cin >> numBins;

  if (method == 1)
  {
    vector<vector<int>> freqBins = equalFrequencyBinning(data, numBins);
    writeCSV("BinByFrequency.csv", freqBins);
  }
  else if (method == 2)
  {
    vector<vector<int>> meanBins = binByMeanBinning(data, numBins);
    writeCSV("BinByMean.csv", meanBins); // Updated output file name
  }
  else
  {
    cout << "Invalid method choice." << endl;
  }

  return 0;
}
