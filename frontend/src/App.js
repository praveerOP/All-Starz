import './App.css';
import React, { Fragment, useEffect, useState } from 'react'
import Navbar from './components/Navbar';
import axios from 'axios'
function App() {
  function hashtags1(){
  //   var hashtags = {
  //     "#1": {
  //       name: 'Nothing Phone 1',
  //       likes: 30000
  //     },
  //     "#2": {
  //       name: 'Sony Bravia 4k OLED',
  //       likes: 20000
  //     },
  //     "#3": {
  //       name: 'Armaf Club De Noit',
  //       likes: 15000
  //     }
  //   }
  //   return(hashtags)
  }
  useEffect(() => {
      // let hashtags = hashtags1();
      let arr = [];
      axios.get("http://127.0.0.1:8000/")
        .then((response) => {
          // console.log("get.data: ",response.data)
          let title = Object.keys(response.data)
          for(let i in response.data[title]){
            arr.push(i)
            document.getElementById('hashtags').innerHTML += '<li>' +i+ '</li>';
          }
          // console.log(arr)
        // title = Object.keys(hashtag_data)
        // dict = Object.values(hashtag_data)
        // console.log("Title: ", title, "dict: ", dict)
        
        // for(const key in hashtag_data[title]){
        //   console.log("key value = ",key, hashtags[key]);
        //   document.getElementById('hashtags').innerHTML += '<li>' + hashtags[key].name + '</li>';
        // }
        // }
      })
      return () => {

        // this now gets called when the component unmounts
    };
    } 
  )
    
  return (
    <div classname = "page">
      {/* <div className="navbar">Navbar</div> */}
      <Navbar/>
      <div className="body">
        <div className="left_prods prods"><p>Left</p></div>
        <div className="right_prods prods"><p>Right</p></div>
      </div>
      <div className="rankings"><p># Rankings</p>
      <ul id="hashtags">
      </ul>
      </div>
      <div className="footer">Footer</div>
    </div>
  );
}

export default App;




