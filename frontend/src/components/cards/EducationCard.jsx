import Card from "./Card";

function EducationCard({ education }) {

    return (

        <Card
            title="Education"
            icon="🎓"
        >

            <p className="text-gray-700 leading-7">

                {typeof education === "string"
                    ? education
                    : JSON.stringify(education, null, 2)}

            </p>

        </Card>

    );

}

export default EducationCard;