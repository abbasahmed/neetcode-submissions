public class MyStack {
    public Queue<int> myQueue = new Queue<int>();

    public MyStack() {
        myQueue = new Queue<int>();
    }
    
    public void Push(int x) {
        this.myQueue.Enqueue(x);
        for(int i = 0; i < this.myQueue.Count - 1; i++){
            this.myQueue.Enqueue(this.myQueue.Dequeue());
        }
    }
    
    public int Pop() {
        return this.myQueue.Dequeue();
    }
    
    public int Top() {
        return this.myQueue.Peek();
    }
    
    public bool Empty() {  
        return this.myQueue.Count == 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Top();
 * bool param_4 = obj.Empty();
 */