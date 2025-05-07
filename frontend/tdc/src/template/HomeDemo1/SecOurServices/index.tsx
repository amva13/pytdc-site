import React from 'react';
import SectionHeading from '../../../components/SectionHeading';
import Content from './Content';

type ServiceData = {
  title: string;
  content: string;
  link: string
};

type SecOurServicesProps = {
  data: ServiceData[];
};

const SecOurServices: React.FC<SecOurServicesProps> = ({ data }) => {
  return (
    <section className="our_services_area section-padding-100-70 clearfix" id="services">
      <div className="container">
        <SectionHeading
          title="PyTDC ML Tasks"
          text="We introduce therapeutics ML tasks, datasets, and benchmarks spanning an unprecedented number of modalities.
          Modalities in PyTDC include but are not limited to: single-cell gene expression atlases,
single-cell chemical and genetic perturbations, clinical trial outcome data, peptide sequence data,
peptidomimetics protein-peptide interaction data from AS-MS spectroscopy, novel 3D
structural protein data, and cell-type-specific protein-protein interaction networks
at single-cell resolution. PyTDC introduces ML tasks taking on open challenges, including the
inferential gap in precision medicine and evaluation on longitudinal data,
model generalization across cell lines and single-cell perturbations that were not encountered during 
model training, and evaluation of models across a broad range of diverse biological
contexts."
        />

        <div className="row">
          {data &&
            data.map((item, key) => (
              <Content key={key} title={item.title} content={item.content} link={item.link}/>
            ))}
        </div>
      </div>
    </section>
  );
};

export default SecOurServices;
