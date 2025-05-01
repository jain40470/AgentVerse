import React, { useState } from "react";

const CodeInput = ( {onSubmit} ) => {

    const [code , setCode] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault(e) // stops default form submission , when reload then u losse your state , so it prevents it
        onSubmit(code)
    }

    return (

        <>
        <form className="code-form" onSubmit={handleSubmit}>
            <textarea className="code-textarea" value={code} onChange={(e) => setCode(e.target.value)} placeholder="Paste your code here..." rows={10} />
             <button className="submit-button" type="submit">Analyze Code</button>
        </form>
        </>

    );

};

export default CodeInput;