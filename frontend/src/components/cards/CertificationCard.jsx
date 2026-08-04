import Card from "./Card";

function CertificationCard({ certifications }) {

    return (

        <Card
            title="Certifications"
            icon="📜"
        >

            <div className="flex flex-wrap gap-3">

                {certifications.map((item, index) => (

                    <span
                        key={index}
                        className="bg-green-100 text-green-700 px-4 py-2 rounded-full"
                    >

                        {item}

                    </span>

                ))}

            </div>

        </Card>

    );

}

export default CertificationCard;