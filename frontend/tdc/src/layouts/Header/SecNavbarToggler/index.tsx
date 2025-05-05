
const Span: React.FC = () => {
  return <span></span>;
};

const SecNavbarToggler: React.FC = () => {
  return (
    <div className="classy-navbar-toggler">
      <span className="navbarToggler">
        <Span />
        <Span />
        <Span />
      </span>
    </div>
  );
};

export default SecNavbarToggler;