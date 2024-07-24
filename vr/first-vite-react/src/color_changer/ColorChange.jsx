import React, { useState } from "react"

function ColorChange() {

    // const color = "red";
    const [color, change] = useState("#FFFFFF");

    function setColor(event) {
        return change(event.target.value)
    }

    return (<>
        <div className="firstDiv">
            <h1 style={{ color: color }}>Color Picker</h1>
            <div className="secondDiv" style={{ backgroundColor: color }}>
                <p>color: {color}</p>
            </div>
            <input type="color" value={color} onChange={setColor} />
        </div>
    </>)
}

export default ColorChange