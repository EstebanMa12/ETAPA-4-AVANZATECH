class HashTable {
    constructor(size) {
        this.data = new Array(size);
    }
    hashMethod(key) {
        let hash = 0;
        for (let i = 0; i < key.length; i++) {
            hash = (hash + key.charCodeAt(i) * i) % this.data.length;
        }
        return hash;
    }
    set(key, value) {
        const address = this.hashMethod(key);
        if (!this.data[address]) {
            this.data[address] = [];
        }
        this.data[address].push([key, value]);
        return this.data;
    }
    get(key) {
        const address = this.hashMethod(key);
        const currentBucket = this.data[address];
        if (currentBucket) {
            for (let i = 0; i < currentBucket.length; i++) {
                if (currentBucket[i][0] === key) {
                    return currentBucket[i][1];
            }
            }
        }
        return undefined;
    }
    remove(key) {
        const address = this.hashMethod(key);
        const currentBucket = this.data[address];
        if (currentBucket) {
            for (let i = 0; i < currentBucket.length; i++) {
                if (currentBucket[i][0] === key) {
                    const element = currentBucket[i][1];
                    delete currentBucket[i][1]
                    return element;
            }
        }
        }
        return undefined;
    }
    delete(key) {
        //* obtengo el hash del address
        const address = this.hashMethod(key)
        //* Obtengo el bucket donde debo buscar el espacio a eliminar
        const currentBucket = this.data[address]
    
        if (currentBucket) {
          //* recorriendo el espacio
            for (let i = 0; i < currentBucket.length; i++) {
                if (currentBucket[i][0] === key) {
                //* guardo el espacio para retornarlo luego
                    let deletedSpace = currentBucket[i]
                //* elimino el espacio
                    delete currentBucket[i]
                //* elimino el espacio vacio para que los demas espacios recorran
                    currentBucket.splice(i, 1)
                    return deletedSpace
                }
          }
        }
      }
    getAllKeys(){
        const keys = []
        for (let i = 0; i < this.data.length; i++) {
            if (this.data[i]) {
                for (let j =0; j < this.data[i].length;j++){
                    console.log(this.data[i][j]);
                    keys.push(this.data[i][j][0])
                }
          }
        }
        return keys
      }
}

const myHashTable = new HashTable(50);
console.log(myHashTable.set('grapes', 1000));
console.log(myHashTable.set('apples', 54));
console.log(myHashTable.set('oranges', 999));
console.log(myHashTable.get('grapes'));
console.log(myHashTable.get('apples'));
console.log(myHashTable.get('oranges'));
console.log(myHashTable.delete('oranges'));
console.log(myHashTable.get('oranges'));
console.log(myHashTable.getAllKeys());
console.log(myHashTable.data);
