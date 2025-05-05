import React from 'react';

type ContactInfoProps = {
  title: string;
  links: { text: string; href: string }[];
};

type PhoneInfoProps = {
  address: string;
  suite: string;
  phone: string;
  email: string;
};

const ContactInfo: React.FC<ContactInfoProps> = ({ title, links }) => (
  <div className="contact_info text-center wow fadeInUp" data-wow-delay="0.2s">
    <h5>{title}</h5>
    {links.map((link, index) => (
      <a key={index} href={link.href}>
        <p>{link.text}</p>
      </a>
    ))}
  </div>
);

const PhoneInfo: React.FC<PhoneInfoProps> = ({ address, suite, phone, email }) => (
  <div className="contact_info text-center wow fadeInUp" data-wow-delay="0.4s">
    <h5>Phone</h5>
    <p>Mailing Address: {address}</p>
    <p>{suite}</p>
    <p>{phone}</p>
    <p>{email}</p>
  </div>
);

const SecContent: React.FC = () => {
  return (
    <div className="col-12 col-md-7">
      {/* Content Info */}
      <div className="contact_info_area d-sm-flex justify-content-between">
        <ContactInfo
          title="NAVIGATE"
          links={[
            { text: "Advertisers", href: "#" },
            { text: "Developers", href: "#" },
            { text: "Resources", href: "#" },
            { text: "Company", href: "#" },
            { text: "Connect", href: "#" },
          ]}
        />

        <ContactInfo
          title="PRIVACY & TOS"
          links={[
            { text: "Advertiser Agreement", href: "#" },
            { text: "Acceptable Use Policy", href: "#" },
            { text: "Privacy Policy", href: "#" },
            { text: "Technology Privacy", href: "#" },
            { text: "Developer Agreement", href: "#" },
          ]}
        />

        <PhoneInfo
          address="xx00 E. Union Ave"
          suite="Suite 1100. Denver, CO 80237"
          phone="+999 90932 627"
          email="support@yourdomain.com"
        />
      </div>
    </div>
  );
};

export default SecContent;
