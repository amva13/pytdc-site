import Image from 'next/image';

type BlogPostProps = {
    img: string;
  };

const BlogPost: React.FC<BlogPostProps> = ({ img }) => {
    return (
      <div className="col-12 col-md-6 col-lg-4" data-aos="fade-up">
        <div className="single-blog-area">
          <div className="blog_thumbnail">
            <Image src={img} alt="Blog Thumbnail" layout="fill" />
          </div>
          <div className="blog-content">
            <div className="post-meta mt-20">
              <p>
                By <a className="post-author">ADMIN</a> <a>Apr 10, 2018</a>{' '}
                <a className="post-comments">7 comments</a>
              </p>
            </div>
            <a href="index-single-blog.html" className="post-title">
              <h4>How to become a successful businessman.</h4>
            </a>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus fugiat at
              vitae, ratione sapiente repellat.
            </p>
            <a href="index-single-blog.html" className="btn dream-btn mt-15">
              Read Details
            </a>
          </div>
        </div>
      </div>
    );
  };

  export default BlogPost;