//import { number } from "prop-types";

let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:


//Function to return a Random number between 1-9
function generateTarget(){
    return Math.floor(Math.random()*10);
}

//Function to compare human and computer guesses to the secret target.  Subtract Guess form the target, take an absolute value and compare to the computer value of the same.  Closest wins, ties go to the human. 
function compareGuesses(humanGuess, cpuGuess, secretTarget){
    
    const humanDiff = getAbsoluteDistance(humanGuess, secretTarget);
    const cpuDiff = getAbsoluteDistance(cpuGuess, secretTarget);

    if(humanDiff <= cpuDiff ){
        return true;
    } else {
        return false;
    }
}



//Function to generate Absolute Value of two numbers
function getAbsoluteDistance(num1, num2){
    return Math.abs(num1 - num2);
}

//Function to receive the winner of a round and increment the necessary score variable by 1
function updateScore(winner){

    if(winner == 'human' ){
        humanScore++;
    } else {
        computerScore++;
    }

}

//Function to increment the current round number by 1.
function advanceRound(){
    currentRoundNumber++;

}