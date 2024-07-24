import propTypes from 'prop-types'

function Cards(props) {
    return (
        <div className="card">
            <img className="card-img" src={props.img} alt="user profile" />
            <h1>Name {props.name} </h1>
            <h3>Age: {props.age} </h3>
            <p>{props.content}</p>
            <h6>Is Alive: {props.IsAlive ? "Yes" : "No"} </h6>
        </div>
    );
};

Cards.propTypes = {
    img: propTypes.string,
    name: propTypes.string,
    age: propTypes.number,
    content: propTypes.string,
    IsAlive: propTypes.bool,
}

export default Cards;