import SecWelcomeMeter from './SecWelcomeMeter'
import SecWhoWeContantPeople from './SecWhoWeContant'

const SecAboutUsClientPeople = (img: string) => {

  return (
    <section className="about-us-area section-padding-0-100 clearfix" id="about">
        <div className="container">
            <div className="row align-items-center">
                
                <SecWelcomeMeter img={img} />

                <SecWhoWeContantPeople />

            </div>
        </div>
    </section>
  );
}

export default SecAboutUsClientPeople;