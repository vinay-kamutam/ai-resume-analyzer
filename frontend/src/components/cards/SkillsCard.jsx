import Card from "./Card";

function SkillsCard({ skills }) {

    return (

        <Card
            title="Technical Skills"
            icon="🛠"
        >

            <div className="flex flex-wrap gap-3">

                {skills.map((skill, index) => (

                    <span
                        key={index}
                        className="bg-blue-100 text-blue-700 px-3 py-2 rounded-full"
                    >
                        {skill}
                    </span>

                ))}

            </div>

        </Card>

    );

}

export default SkillsCard;