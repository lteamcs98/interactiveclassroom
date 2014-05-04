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

function findMax(arrayOfValues)
{
	var max = arrayOfValues[0];
	for (var i = 0; i < arrayOfValues.length; i++)
	{
		if (arrayOfValues[i] > max) max = arrayOfValues[i];
	}
	return max;
}


function getSquare(someNumber)
{
	return someNumber*someNumber;
}

function squareList(numbers)
{
	for(i in numbers)
	{
		numbers[i] = getSquare(numbers[i]);
	}
	return numbers;
}

function averageOfThree(arg0, arg1, arg2)
{
	var sum = arg0 + arg1 + arg2;

    return sum/3;
}

function mergesort(values)
{
    // Terminal case: 0 or 1 item arrays don't need sorting
    if (values.length < 2) {
        return values;
    }
    var middle = Math.floor(values.length / 2),
        left    = values.slice(0, middle),
        right   = values.slice(middle);

    return merge(mergesort(left), mergesort(right));
}

function merge(left, right)
{
    var result  = [],
        il      = 0,
        ir      = 0;

    while (il < left.length && ir < right.length){
        if (left[il] < right[ir]){
            result.push(left[il++]);
        } else {
            result.push(right[ir++]);
        }
    }
    return result.concat(left.slice(il)).concat(right.slice(ir));
}

function how_rich(initMoney, rate, years)
{
  var totalMoney = initMoney;

  for(var i = 0; i < years; i++){

    totalMoney = totalMoney * rate;

  }

  return totalMoney;
}

function portia(brutusInitMoney, portiaInitMoney, brutusRate, portiaRate)
{
  var brutusTotal = brutusInitMoney;
  var portiaTotal = portiaInitMoney;

  for(var years = 0; brutusTotal < portiaTotal; years++){

    brutusTotal = brutusTotal * brutusRate;
    portiaTotal = portiaTotal * portiaRate;

  }

  return years;
}

function reverse(str)
{
	var reversedString = "";
    for (var i = str.length - 1; i >= 0; i--)
    {
        reversedString = reversedString.concat(str[i]);
    }
    return reversedString;
}
