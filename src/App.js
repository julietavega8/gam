import logo from './logo.svg';
import './App.css';
import Button from './Components';

function App() {
  const handleClick = () => {
    alert('guardar');
  }
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          te damos la
          </p>
        <button text="cancelar" onClick={()=> alert('Hicieron click')}></button>
        <button text="Guardar" onClick={handleClick}></button>
      </header>
    </div>
  );
}

export default App;

















