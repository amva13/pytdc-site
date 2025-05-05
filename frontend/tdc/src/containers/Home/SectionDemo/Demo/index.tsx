import Image from 'next/image';
import Link from 'next/link';

interface DemoProps {
  img: string;
  path: string;
}

const Demo: React.FC<DemoProps> = ({ img, path }) => {
  return (
    <div className="col-lg-4 col-md-6 col-sm-12">
      <div className="demo-item">
        <Link href={path} passHref>
          <a>
            <Image src={img} alt="demo" className="img-responsive" layout="fill" />
          </a>
        </Link>
        <div className="preview-btn-wrapper text-center">
          <Link href={path} passHref>
            <a className="preview-demo">
              View demo <i className="fa fa-long-arrow-right"></i>
            </a>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Demo;
