import React , {useState} from "react"
import {fetchYtUrl} from '../../Utils/ytsummary_api'
import YTUrlInput from './YTUrlInput' 
import SummaryDisplay from "./SummaryDisplay"

const YTAgent = () => {

    const [content , SetContent] = useState(null)

    const handleSubmit = async (url) => {
        const response  = await fetchYtUrl(url)
        console.log(response)
        SetContent(response);
    }

    return(<>

    <div className="max-w-4xl mx-auto p-6">
        <h1 className="text-3xl font-semibold mb-4 text-center text-gray-800">YT Intelligence Agent</h1>
        <div className="flex flex-col space-y-6 h-160 overflow-y-auto">
         <YTUrlInput onSubmit={handleSubmit} />
         {content && <SummaryDisplay content={content} />}
        </div>
    </div>
        
    </>)
}


export default YTAgent;