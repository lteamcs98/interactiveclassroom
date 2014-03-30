var findMax = function(numbArray)
{
	var max = numbArray[0];
	for (var i = 0; i < numbArray.length; i++)
	{
		if (numbArray[i] > max) max = numbArray[i];
	}
	return max;
}

function findMaxFive(numbArray)
{
	var maxArray = [];
	var curMinMax;

	for (var j = 0; j < 5; j++)
	{
		var curMax = 0;

		for (var i = 0; i < numbArray.length; i++)
		{
			if (numbArray[i] > curMax)
			{
				if (j > 0 && numbArray[i] < curMinMax)
					curMax = numbArray[i];
				else if (j == 0)
					curMax = numbArray[i];
			}
		}
		curMinMax = curMax;
		maxArray[j] = curMax;
	}
    return maxArray;
}