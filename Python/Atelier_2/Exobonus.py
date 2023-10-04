def close_to_zero(myList:list) -> float :
    """_summary_

    Args:
        myList (list): _description_

    Returns:
        float: _description_
    """
    petit=myList[0]
    for i in myList:
        if abs(i) < abs(petit):
            petit=i
    return petit

lst_test=[2.5,12,3,-4,5,-1.7]
lst_test2=[11,-9,6,1,-2,-3,10]
print(close_to_zero(lst_test))
print(close_to_zero(lst_test2))