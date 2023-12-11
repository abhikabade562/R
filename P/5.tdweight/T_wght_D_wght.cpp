#include <iostream>
#include <fstream>
#include <sstream>
#include <map>

using namespace std;

// A struct to represent cell data in the CSV file
struct CellData
{
    int count;
    int tWeight;
    int dWeight;
};

// Function to read data from the input CSV file into provided data structures
void readCSVData(const string &filename, map<string, map<string, CellData>> &cellData,
                 map<string, int> &columnTotal, map<string, int> &rowTotal)
{
    fstream file(filename, ios::in);
    if (!file.is_open())
    {
        cout << "Couldn't open file: " << filename << endl;
        return;
    }

    string line, row, col, count;
    int val;

    int lineNumber = 0;

    while (getline(file, line))
    {
        stringstream str(line);

        if (lineNumber == 0)
        {
            lineNumber++;
            continue; // Skip the header line
        }

        getline(str, row, ',');
        getline(str, col, ',');
        getline(str, count, ',');

        val = stoi(count);

        cellData[row][col].count += val;
        columnTotal[col] += val;
        rowTotal[row] += val;
    }
}

// Function to write the result to an output CSV file
void writeCSVResult(const string &filename, const map<string, map<string, CellData>> &cellData,
                    const map<string, int> &columnTotal, const map<string, int> &rowTotal)
{
    ofstream outputFile(filename, ios::out);

    outputFile << "Column\\Row, Count, T-Weight, D-Weight, Count, T-Weight, D-Weight, Count, T-Weight, D-Weight" << endl;

    for (const auto &rowEntry : rowTotal)
    {
        const string &row = rowEntry.first;
        outputFile << row << ",";

        for (const auto &colEntry : columnTotal)
        {
            const string &col = colEntry.first;
            const CellData &cell = cellData.at(row).at(col);

            outputFile << cell.count << ",";
            outputFile << ((float)cell.count / rowTotal.at(row)) * 100 << "%,";
            outputFile << ((float)cell.count / colEntry.second) * 100 << "%,";
        }

        outputFile << rowTotal.at(row) << ","
                   << "100%, " << ((float)rowTotal.at(row) / rowTotal.at(rowTotal.begin()->first)) * 100 << "%" << endl;
    }

    outputFile << "Total,";

    for (const auto &colEntry : columnTotal)
    {
        outputFile << colEntry.second << ",";
        outputFile << ((float)colEntry.second / columnTotal.at(columnTotal.begin()->first)) * 100 << "%,";
        outputFile << "100%,";
    }

    outputFile << columnTotal.at(columnTotal.begin()->first) << ",100%, 100%" << endl;
}

int main()
{
    map<string, map<string, CellData>> cellData;
    map<string, int> columnTotal;
    map<string, int> rowTotal;

    readCSVData("Input_File.csv", cellData, columnTotal, rowTotal);
    writeCSVResult("Output_File.csv", cellData, columnTotal, rowTotal);

    cout <<endl<<"Check 'Output_File.csv' for the result" << endl;

    return 0;
}
