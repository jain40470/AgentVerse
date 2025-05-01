import { useState } from 'react'
import './App.css'

import ChatContainer from './Components/Chatbot/ChatContainer'
import CodeReview from './Components/CodeReviewer/CodeReview'

const Home = () => <div className="p-4 text-xl font-semibold">Welcome to Home!</div>

function App() {

  const [selected, setSelected] = useState('Home')
  
  const components = {
    Home: <Home />,
    BasicChatBot : <ChatContainer/> ,
    CodeReviewer : <CodeReview/> ,
    YT_Video_Summary : <Home/>, 
    Stock_Intelligence : <Home/>,
  }

  const menuItems = Object.keys(components)

  return (
    <>
  
    <div className="flex flex-col md:flex-row h-screen bg-gray-800">
      
      <div className="w-full md:w-1/4 bg-gray-800 text-white p-4 flex flex-col justify-center items-center overflow-y-auto">
        <h1 className="text-5xl font-bold mb-6 mt-30"> Agent Verse </h1>
        <ul className="flex flex-col justify-center items-center space-y-6 flex-grow">
         {menuItems.map((item) => (
           <li key={item} className={`cursor-pointer font-bold text-2xl hover:text-yellow-400 ${selected === item ? 'text-yellow-300 font-semibold' : ''}`}
          onClick={() => setSelected(item)}
          > {item} </li>
        ))}
       </ul>
      </div>

      <div className="w-full md:w-3/4 bg-gray-100 flex items-center justify-center overflow-y-auto">
        <div className="w-full max-w-5xl p-8 mt-10">
          {components[selected]}
        </div>
      </div>

    </div>

    </>
  )

}

export default App
