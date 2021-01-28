console.log("hello World")
//let str1="aaa"
//console.log(str1)
/*if(true){
    console.log(true)
}
else{

}
switch (key) {
    case value:
        
        break;

    default:
        break;
}          

for (let index = 0; index < array.length; index++) {
    const element = array[index];
    
}
while (condition) {
    
}
*/
/*let str1="Hello World"
let strsplit=split.str1(" ")
console.log(strsplit)*/

let arr1=[1,2,3,4,5,6,7]
function myFunc(element){
    console.log("elements",element)
}
let myfunc=(element)=>{
    console.log("elements",element)  
}

arr1.forEach(myfunc)
arr1.forEach((element)=>{
    console.log("elements",element)

});
let arr2=arr1.map((element)=>{
    return element*2;

});
let arr3=arr1.map((element)=>{
    return element>2;

});
console.log(arr2)
console.log(arr3)
let arr4=arr1.reduce((acc,element)=>{
    return acc+=element;

},0);
console.log(arr4)

let arr5=[
    {
        name:"deneme",
        surname:"dsjnflfç",
        id:"id1"
},
    {  name:"deneme",
       surname:"dsjnflfç",
       id:"id2"
},
    {
        name:"deneme",
        surname:"dsjnflfç",
        id:"id3"
},
    {
        name:"deneme",
        surname:"dsjnflfç",
        id:"id4"
}


];
let result=arr5.map((element)=>{
    return element.name });

console.log(result);

let result2=arr5.reduce((acc, element)=>{
    return {
        ...acc,
        [element.id] :element
    }

},{});
console.log(result2);
console.log(result2.id3.name)
let obj1={
    id1: { name: 'deneme', surname: 'dsjnflfç' },
  id2: { name: 'deneme', surname: 'dsjnflfç' },
  id3: { name: 'deneme', surname: 'dsjnflfç' },
  id4: { name: 'deneme', surname: 'dsjnflfç' }
}
let result3=Object.keys(obj1).map((key)=>{
    return {
        ...obj1[key],
        id:key
    }

});
console.log(result3)

//pointer
let arr6=[1,2,3,4]
console.log(arr6[2]);
arr6[2]=100;
console.log(arr6);
arr7=[...arr6]
arr6[1]=0
console.log(arr7)

class Student{
    
}

