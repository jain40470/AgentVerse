import React , {useState} from "react"
import {fetchYtUrl} from '../../Utils/ytsummary_api'
import YTUrlInput from './YTUrlInput' 
import SummaryDisplay from "./SummaryDisplay"

const YTAgent = () => {

    const [content , SetContent] = useState(null)
    const [loading, setLoading] = useState(false);


    const handleSubmit = async (url) => {

        setLoading(true);
        try {
            const response = await fetchYtUrl(url);
            console.log(response);
            SetContent(response);
        } catch (error) {
            console.error("Error fetching YouTube summary:", error);
        } finally {
            setLoading(false);
        }
        // const response  = await fetchYtUrl(url)
        // console.log(response)
        // SetContent(response);
    }

    return(<>

    {loading && (
        <div className="flex justify-center items-center">
        <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-blue-500"></div>
        </div>
    )}

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