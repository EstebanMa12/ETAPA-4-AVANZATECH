/* const array = [1,2,3]
console.log(array); */

class MyArray {
    constructor(){
        this.length =0;
        this.data = {}
    }
    get(index){
        return this.data[index]
    }

    push(item){
        this.data[this.length]=item
        this.length ++;
        return this.data
    }
    pop(){
        const lastItem = this.data[this.length-1]
        delete this.data[this.length-1]
        this.length--;
        return lastItem
    }
    delete(index){
        const item = this.data[index]
        this.shiftIndex(index)
        return item
    }
    shiftIndex(index){
        for (let i = index; i < this.length-1;i++){
            this.data[i] = this.data[i + 1]
        }
        delete this.data[this.length - 1]
        this.length--;
    }
}

const myArray = new MyArray();
console.log(myArray.push('Diego'));
console.log(myArray.push('Karen'));
console.log(myArray.push('Oscar'));
// console.log(myArray.pop());
console.log(myArray);
console.log(myArray.delete(0));
console.log(myArray);
console.log(myArray.push('Esteban'));
console.log(myArray.push('Luis'));
console.log(myArray.push('Pedro'));
console.log(myArray.delete(2));
console.log(myArray);