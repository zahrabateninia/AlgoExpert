// Each integer of the array represents a jump of its value in the array
// ex: a value of 3 represents a jump of 3 indices forward in the array
// if a jump spills past the array bounds, it wraps over to the other side
// this function should return a boolean representing whether the jumps in array form a SINGLE CYCLE.
// SINGLE CYCLE occurs, if starting at any index in the array and following the jumps, every element in the array is visited exactly once, before landing back on the starting index

function hasSingleCycle(array) {
    // O(n) time | O(1) space 
    let numElementsVisited = 0;
    let currentIdx = 0; // you can start form any index in your array, I choose the first index
    while( numElementsVisited < array.length) {
      // if we visited more than one element and we find ourselves at index 0
      if(numElementsVisited > 0 && currentIdx == 0){
        return false; // we deal with multiple cycles
      }
      numElementsVisited += 1;
      currentIdx = getNextIdx(currentIdx, array)
    }
    return currentIdx === 0; // once we visited n elements, we have to be back at the starting index(0)
  }
  
  function getNextIdx(currentIdx, array){
    // naive solution which is wrong is : jump = array[currentIdx] and nextIdx = currentIdx + jump#
    // careful of edge cases: we have gigantic and negative integers as well
    let jump = array[currentIdx]
    let nextIdx = (currentIdx + jump) % array.length; // this % array.length() handles big integers
    if(nextIdx >= 0){
      return nextIdx;
    }else{
      return nextIdx + array.length; // handle negative jumps(get the positive equivalent of that)
    } 
  }
    
  
