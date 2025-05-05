type LiAProps = {
	path: string;
	nameLink: string;
  };
  
  const LiA: React.FC<LiAProps> = ({ path, nameLink }) => {
	return <li><a href={path}>{nameLink}</a></li>;
  };
  
  type SecMenuProps = {
	data: { path: string; nameLink: string }[];
  };
  
  const SecMenu: React.FC<SecMenuProps> = ({ data }) => {
	return (
	  <div className="classy-menu">
		<div className="classycloseIcon">
		  <div className="cross-wrap">
			<span className="top"></span>
			<span className="bottom"></span>
		  </div>
		</div>
  
		<div className="classynav">
		  <ul id="nav" data-aos="fade-down">
			{data && data.map((item, key) => (
			  <LiA
				key={key}
				path={item.path}
				nameLink={item.nameLink}
			  />
			))}
		  </ul>
  
		  <a className="btn login-btn ml-50">Log in</a>
		</div>
	  </div>
	);
  };
  
  export default SecMenu;