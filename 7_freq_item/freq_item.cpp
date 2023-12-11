#include <bits/stdc++.h>
#include <map>
using namespace std;

ifstream inputFile;                
double minFrequency;           
vector<set<string>> transactionData;
set<string> products;             
map<string, int> frequency;       

// Function to split a string into words based on alphanumeric characters.
vector<string> splitWords(string str)
{
    vector<string> wordList;
    string word = "";
    int i = 0;
    while (str[i])
    {
        if (isalnum(str[i]))
            word += str[i];
        else
        {
            if (!word.empty())
                wordList.push_back(word);
            word = "";
        }
        i++;
    }

    if (!word.empty())
        wordList.push_back(word);

    return wordList;
}

// Function to combine elements in a vector into a string, excluding the one at 'exclude' index.
string combine(vector<string> &arr, int exclude)
{
    string result;
    for (int i = 0; i < arr.size(); i++)
    {
        if (i != exclude)
            result += arr[i] + " ";
    }
    result = result.substr(0, result.size() - 1);
    return result;
}

// Function to clone a set and return a copy.
set<string> cloneSet(set<string> &s)
{
    set<string> duplicate;
    for (set<string>::iterator it = s.begin(); it != s.end(); it++)
        duplicate.insert(*it);
    return duplicate;
}

// Function to generate frequent itemsets of size k based on candidate itemsets of size k-1.
set<string> aprioriGenerate(set<string> &sets, int k)
{
    set<string> set2;
    for (set<string>::iterator it1 = sets.begin(); it1 != sets.end(); it1++)
    {
        set<string>::iterator it2 = it1;
        it2++;
        for (; it2 != sets.end(); it2++)
        {
            vector<string> v1 = splitWords(*it1);
            vector<string> v2 = splitWords(*it2);

            bool allEqual = true;
            for (int i = 0; i < k - 1 && allEqual; i++)
            {
                if (v1[i] != v2[i])
                    allEqual = false;
            }

            v1.push_back(v2[k - 1]);
            if (v1[v1.size() - 1] < v1[v1.size() - 2])
                swap(v1[v1.size() - 1], v1[v1.size() - 2]);

            for (int i = 0; i < v1.size() && allEqual; i++)
            {
                string temp = combine(v1, i);
                if (sets.find(temp) == sets.end())
                    allEqual = false;
            }

            if (allEqual)
                set2.insert(combine(v1, -1));
        }
    }
    return set2;
}

int main()
{
    inputFile.open("item_set_input.csv", ios::in); // Open the input file for reading.

    if (!inputFile.is_open())
    {
        perror("Error in opening file: "); // Print an error message if the file cannot be opened.
    }
    cout << "Minimum Frequency (%): ";
    cin >> minFrequency; // Read the minimum frequency from the user.

    string line;
    while (!inputFile.eof())
    {
        getline(inputFile, line);

        vector<string> items = splitWords(line);

        set<string> itemSet;
        for (int i = 0; i < items.size(); i++)
            itemSet.insert(items[i]);
        transactionData.push_back(itemSet); // Store the transaction data in the 'transactionData' vector.

        for (set<string>::iterator it = itemSet.begin(); it != itemSet.end(); it++)
        {
            products.insert(*it); // Store unique products in the 'products' set.
            frequency[*it]++;     // Increment the frequency of each product in the 'frequency' map.
        }
    }
    inputFile.close(); // Close the input file.

    cout << "Number of transactions: " << transactionData.size() << endl;
    minFrequency = minFrequency * transactionData.size() / 100; // Calculate the minimum frequency threshold.
    cout << "Minimum frequency: " << minFrequency << endl;

    queue<set<string>::iterator> q;
    for (set<string>::iterator it = products.begin(); it != products.end(); it++)
        if (frequency[*it] < minFrequency)
            q.push(it);

    while (q.size() > 0)
    {
        products.erase(*q.front()); // Remove infrequent products from the 'products' set.
        q.pop();
    }

    int pass = 1;
    cout << "\nFrequent " << pass++ << "-item set: \n";
    for (set<string>::iterator it = products.begin(); it != products.end(); it++)
        cout << "{" << *it << "} " << frequency[*it] << endl; // Display frequent 1-itemsets.

    int i = 2;
    set<string> prev = cloneSet(products);

    while (i)
    {
        set<string> cur = aprioriGenerate(prev, i - 1); // Generate candidate itemsets of size 'i'.

        if (cur.size() < 1)
        {
            break;
        }

        for (set<string>::iterator it = cur.begin(); it != cur.end(); it++)
        {
            vector<string> items = splitWords(*it);

            int total = 0;
            for (int j = 0; j < transactionData.size(); j++)
            {
                bool present = true;
                for (int k = 0; k < items.size() && present; k++)
                    if (transactionData[j].find(items[k]) == transactionData[j].end())
                        present = false;
                if (present)
                    total++;
            }
            if (total >= minFrequency)
                frequency[*it] += total;
            else
                q.push(it);
        }

        while (q.size() > 0)
        {
            cur.erase(*q.front());
            q.pop();
        }

        bool flag = true;

        for (set<string>::iterator it = cur.begin(); it != cur.end(); it++)
        {
            vector<string> items = splitWords(*it);

            if (frequency[*it] < minFrequency)
                flag = false;
        }

        if (cur.size() == 0)
            break;

        cout << "\n\nFrequent " << pass++ << "-item set: \n";
        for (set<string>::iterator it = cur.begin(); it != cur.end(); it++)
            cout << "{" << *it << "} " << frequency[*it] << endl; // Display frequent k-itemsets.

        prev = cloneSet(cur);
        i++;
    }
    ofstream outputFile("item_set_output.csv", ios::out); // Open an output file for writing.

    for (auto it = prev.begin(); it != prev.end(); it++)
    {
        outputFile << "{" << *it << "}" << endl; // Write frequent itemsets to the output file.
    }

    return 1;
}
