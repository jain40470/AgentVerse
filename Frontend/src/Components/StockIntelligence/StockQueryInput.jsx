import React , {useState} from 'react'


const StockQueryInput = ( {onSubmit} ) => {
    
    const [query , setQuery ] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(query);
    }

    return (<>
    
        <form onSubmit={handleSubmit} className="mb-6">
        <input
        className="w-full max-w-3xl p-4 min-h-[100px] text-base md:text-lg border-2 border-gray-300 rounded-2xl shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Type your stock market query here..."
        />
        <button
                type="submit"
                className="w-full mt-4 py-2 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600"
        >
            Get Report
          </button>
        </form>
      </>);

}

export default StockQueryInput;

//