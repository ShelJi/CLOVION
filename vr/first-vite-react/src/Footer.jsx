function Footer() {
    return (
        <footer>
            <p>
                &copy; {new Date().getDate()} {new Date().getDay()} {new Date().getFullYear()} Im at the bottom
            </p>
        </footer>
    );
};

export default Footer