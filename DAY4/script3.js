function printTable(num)
{
    for(let i=0;i<=10;i++)
    {
        console.log(num+"*"+i+"="+num*i);
    }
}
const num= prompt("Enter a number: ")
printTable(num)