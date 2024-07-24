import React, { useState } from 'react'

function Game() {

    const [count, setCount] = useState(0);

    const increment = () => {
        setCount(count + 1);
    }
    const decrement = () => {
        setCount(count -1);
    }
    const reset = () => {
        setCount(0);
    }

    return (
        <>
            <h1>{count}</h1>
            <button className="decrement" onClick={decrement}>Decrement</button>
            <button className="reset" onClick={reset}>Reset</button>
            <button className="increment" onClick={increment}>Increment</button>
        </>
    );
}

export default Game