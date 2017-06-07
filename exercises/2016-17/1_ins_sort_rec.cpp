// InsertionSort
void InsertionSort(int A[]){

for j = 2 to A.length
    key = A[j];
    i = j-1;
    while (i>0 && A[i]>key){
        A[i+1] = A[i];
        i = i-1;
    }
    A[i+1] = key;
}

//RecursiveInsertionSort

void RecursiveInsertionSort(int A[], int n){
    if(n <=1)
        return;
    
    RecursiveInsertionSort(A,n-1);
    
    int last = A[n-1];
    int j = n-2;
 
    compareKey(A,j,last);
    A[j+1] = last;
}

void compareKey(int A[], int& j, int l){
    
    if(j<0)
        return;
    
    A[j+1] = A[j];
    compareKey(A, j--,l);
}

