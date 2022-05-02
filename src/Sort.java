import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Random;

public class Sort {
    public static void main(String[] args) {
        int n = (int)Math.pow(2, 16);
        int[] array = new int[n];
        Random random = new Random();
        for (int i=0; i < n; i++){
            array[i] = random.nextInt(n);
        }
        Sort sort = new Sort();
        long start = System.currentTimeMillis();
        sort.BubbleSort(array);
        long end = System.currentTimeMillis();
        System.out.println("소요 시간 : " + (end - start)+ " ms");
        for (int i=0; i<array.length; i++){
            System.out.printf(array[i] + " ");
        }
    }
    public void BubbleSort(int[] array){
        for (int i=0; i<array.length; i++){
            for (int j=0; j<array.length-i-1; j++){
                if (array[j] > array[j+1]){
                    int temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
    }
    public void SelectionSort(int[] array){
        for (int i=0; i<array.length; i++){
            int min = array[i];
            int index = i;
            for (int j=i+1; j<array.length; j++){
                if (min > array[j]){
                    min = array[j];
                    index = j;
                }
            }
            int temp = array[i];
            array[i] = array[index];
            array[index] = temp;
        }
    }
    public void InsertionSort(int[] array){
        for (int i=1; i<array.length; i++){
            int current_element = array[i];
            int j = i - 1;
            while (j >= 0 && array[j] > current_element){
                array[j+1] = array[j];
                j -= 1;
            }
            array[j+1] = current_element;
        }
    }
    public void ShellSort(int[] array){
        int[] gap = {5,4,3,2,1};
        for (int h : gap) {
            for (int i=h; i<array.length; i++){
                int current_element = array[i];
                int j = i;
                while (j >= h && array[j-h] > current_element){
                    array[j] = array[j-h];
                    j -= h;
                }
            array[j] = current_element;
            }
        }
    }
    public void HeapSort(int[] array){
        PriorityQueue heap = new PriorityQueue();
        int index = 0;
        for(int i : array) {
            heap.add(i);
        }
        while(!heap.isEmpty()){
            array[index] = (int)heap.remove();
            index++;
        }
    }
    public void QuickSort(int[] array){
        Arrays.sort(array);
    }
}
