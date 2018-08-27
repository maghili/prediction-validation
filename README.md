# prediction-validation
prediction validation of a data science model

The method that I have chosen here to compile the data in the fastest possible way is to use python dictionaries inside dictionaries.

I put each of the Actual data `actual.txt` and the redicted data `predicted.txt`, inside separate dictionaries with the `time` as their key, and then within ech of those dictionaries I create another dictionary at each `time` with `stock` as the key and then the value of the `stock` goes into them.

```
ActualData = {time1: {stock1: value, stock2: value, ...}, time2: {stock1: value, ...},\
..., timen: {stock1: value, ...}}

PredictedData = {time1: {stock1: predict, stock2: predict, ...}, time2: {stock1: predict, ...},\
..., timen: {stock1: predict, ...}}
```
resembling the following table:
<table>
  <tr>
    <th colspan = 3>time1</th>
    <th colspan = 3>time2</th>
    <th > ... </th>
    <th colspan = 3>timen</th>
  </tr>
  <tr>
     <td>stock1</td>
     <td>stock2</td>
     <td> ... </td>
     <td>stock1</td>
     <td>stock2</td>
     <td> ... </td>
     <td> ... </td>
     <td>stock1</td>
     <td>stock2</td>
     <td> ... </td>
  </tr>
  <tr>
    <td>value</td>
     <td>value</td>
     <td> ... </td>
     <td>value</td>
     <td>value</td>
     <td> ... </td>
     <td> ... </td>
     <td>value</td>
     <td>value</td>
     <td> ... </td>
  </tr>
</table>

writing it this way has the advantage that calling the values have time complexity of *O(1)*, and therefore the whole process of going over all the time slots and stocks which form the total number of data, and each time doing it for the duration of a time window from `window.txt` we get to have time complexitiy of the order of `2*n*w`, where `n` is the total number of data, `w` is the window length and is basically how many times a data will be called, and it needs to be done for both Actual data and Predicted data, therefore in the common notation the code is *O(w.n)*.
