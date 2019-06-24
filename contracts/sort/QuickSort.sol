pragma solidity ^0.4.24;

contract QuickSort {
    event finish(uint size, uint signature);
    uint counter;

    function sort(uint size, uint signature) public {
        uint[] memory data = new uint[](size);
        for (uint x = 0; x < data.length; x++) {
            data[x] = size-x;
        }
        quickSort(data, 0, data.length - 1);
        emit finish(size, signature);
    }

    function quickSort(uint[] arr, uint left, uint right) internal {
        uint i;
        uint j;
        uint pivot;

        if (left < right){
            pivot = left;
            i = left;
            j = right;

            while (i < j) {
                while (arr[i] <= arr[pivot] && i < right) i++;
                while (arr[j] > arr[pivot]) j--;
                if (i < j) {
                    (arr[i], arr[j]) = (arr[j], arr[i]);
                }
            }

            (arr[pivot], arr[j]) = (arr[j], arr[pivot]);

            if (j > 1) quickSort(arr, left, j-1);
            quickSort(arr, j+1, right);
        }
    }

    function  empty() public {
        counter++;
    }
}
