import React , {useState} from 'react'


const YTUrlInput = ( {onSubmit} ) => {
    
    const [url , setUrl ] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(url);
    }

    return (<>
        <form onSubmit={handleSubmit} className="mb-6">
        <input
        className="w-full max-w-3xl p-4 text-base md:text-lg border-2 border-gray-300 rounded-2xl shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter YouTube video URL"
        />
        <button
            type="submit"
            className="w-full mt-4 py-2 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600"
        >
        Get Summary
        </button>
        </form>
      </>);

}

export default YTUrlInput;