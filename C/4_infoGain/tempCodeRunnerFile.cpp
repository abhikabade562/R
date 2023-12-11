for (auto it = childCounts.begin(); it != childCounts.end(); ++it)
    {
        string childName = it->first;
        double positiveChild = it->second["Yes"];
        double negativeChild = it->second["No"];
        double totalChild = positiveChild + negativeChild;

        double childEntropyPart = calculateInformationEntropy(positiveChild, negativeChild);

        childEntropy += (totalChild / totalParent) * childEntropyPart;
    }

    cout << "Weighted Child Entropy: " << childEntropy << "\n";