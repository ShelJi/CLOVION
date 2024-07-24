import Header from './Header.jsx'
import Footer from './Footer.jsx'
import Cards from './Cards.jsx'
import img from './assets/queen.jpg'

function App() {
  return (
    <>
      {/* <Header></Header> */}
      {/* <Footer></Footer> */}
      <Header />
      <Cards img={img}
        name="PenQueen"
        content="Im mrs penqueen living in my house which is in my place"
        IsAlive={true}
        age={2}
      />
      <Cards />
      <Footer />
    </>
  );
}

export default App
