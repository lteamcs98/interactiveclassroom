var findMax = function(numbArray)
{
	var max = numbArray[0];
	for (var i = 0; i < numbArray.length; i++)
	{
		if (numbArray[i] > max) max = numbArray[i];
	}
    return max;
}