import React , {useState} from "react"
import {fetchStockquery} from '../../Utils/Stock_api'
import StockQueryInput from './StockQueryInput'
import ReportDisplay from './ReportDisplay'

const StockAgent = () => {

    const [report , SetReport] = useState(null)

    const handleSubmit = async (userquery) => {
        const response  = await fetchStockquery(userquery)
        SetReport(response.report);
    }

    return(<>

    <div className="max-w-4xl mx-auto p-6">
        <h1 className="text-3xl font-semibold mb-4 text-center text-gray-800">Stock Intelligence Agent</h1>
        <div className="flex flex-col space-y-6 h-160 overflow-y-auto">
         <StockQueryInput onSubmit={handleSubmit} />
         {report && <ReportDisplay report={report} />}
        </div>
    </div>
        
    </>)
}


export default StockAgent;