import Card from "./Card";

function SummaryCard({ summary }) {

    return (

        <Card
            title="Professional Summary"
            icon="👨"
        >

            <p className="text-gray-700 leading-7">

                {summary}

            </p>

        </Card>

    );

}

export default SummaryCard;