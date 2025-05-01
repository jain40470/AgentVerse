import { useState } from 'react'
import './App.css'
import ChatContainer from './Components/Chatbot/ChatContainer'

const Home = () => <div className="p-4 text-xl font-semibold">Welcome to Home!</div>

function App() {

  const [selected, setSelected] = useState('Home')
  
  const components = {
    Home: <Home />,
    BasicChatBot : <ChatContainer/> ,
    CodeReviewer : <Home/> ,
    YT_Video_Summary : <Home/>, 
    Stock_Intelligence : <Home/>,
  }

  const menuItems = Object.keys(components)

  return (
    <>
  
    <div className="flex flex-col md:flex-row h-screen">
      <div className="w-full md:w-1/4 bg-gray-800 text-white p-4 flex flex-col justify-center items-center">
        <h1 className="text-5xl font-bold mb-6 mt-8"> Agent Verse </h1>
        <ul className="flex flex-col justify-center items-center space-y-6 flex-grow">
         {menuItems.map((item) => (
           <li key={item} className={`cursor-pointer font-bold text-2xl hover:text-yellow-400 ${selected === item ? 'text-yellow-300 font-semibold' : ''}`}
          onClick={() => setSelected(item)}
          > {item} </li>
        ))}
       </ul>
      </div>

    <div className="w-full md:w-3/4 bg-gray-100 flex items-center justify-center">
      <div className="w-full max-w-5xl p-8 text-center">
        {components[selected]}
      </div>
    </div>
    </div>

    </>
  )

}

export default App
