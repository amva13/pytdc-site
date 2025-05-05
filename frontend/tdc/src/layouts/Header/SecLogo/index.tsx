import Image from 'next/image';

const SecLogo = (img: string) => {

  return (
    	<a className="nav-brand"  ><Image src={img} alt="logo" layout="fill" /> </a>
    );
}

export default SecLogo;