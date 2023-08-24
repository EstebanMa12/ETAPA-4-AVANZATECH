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
    unshift(item) {
        if (!item) {
            return this.length
        }
        if (this.length !== 0) {
            for (let i = this.length - 1; i >= 0; i--){
            this.data[i+1] = this.data[i]
            }
        }
        this.data[0] = item
        this.length++
        return this.length
        // Tu código aquí 👈  
    }
    shift(){
        if (this.length == 0) {
            return undefined
        } else {
            const deletedNumber = this.data[0]
            for (let i = 0; i < this.length; i++){
            this.data[i] = this.data[i+1]
            }
            delete this.data[length - 1]
            this.length--
            return deletedNumber
        }
        
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