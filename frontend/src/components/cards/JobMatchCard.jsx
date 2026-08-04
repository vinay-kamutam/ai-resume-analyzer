import Card from "./Card";
import ProgressBar from "./ProgressBar";

function JobMatchCard({ match }) {

    if (!match) return null;

    const score = match.match_percentage;

    let color = "bg-red-500";
    let textColor = "text-red-600";

    if (score >= 80) {
        color = "bg-green-500";
        textColor = "text-green-600";
    }
    else if (score >= 60) {
        color = "bg-yellow-500";
        textColor = "text-yellow-600";
    }

    return (

        <Card
            title="Job Match"
            icon="💼"
        >

            <div className="text-center mb-6">

                <h1 className={`text-6xl font-bold ${textColor}`}>

                    {score}%

                </h1>

            </div>

            <ProgressBar
                value={score}
                color={color}
            />

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">

                <div>

                    <h3 className="font-bold text-green-600 mb-3">
                        ✅ Matching Skills
                    </h3>

                    {match.matching_skills?.length ? (

                        <ul className="list-disc ml-5 space-y-2">

                            {match.matching_skills.map((item, index) => (

                                <li key={index}>{item}</li>

                            ))}

                        </ul>

                    ) : (

                        <p className="text-gray-500 italic">
                            No matching skills found.
                        </p>

                    )}

                </div>

                <div>

                    <h3 className="font-bold text-red-600 mb-3">
                        ❌ Missing Skills
                    </h3>

                    {match.missing_skills?.length ? (

                        <ul className="list-disc ml-5 space-y-2">

                            {match.missing_skills.map((item, index) => (

                                <li key={index}>{item}</li>

                            ))}

                        </ul>

                    ) : (

                        <p className="text-gray-500 italic">
                            No missing skills.
                        </p>

                    )}

                </div>

            </div>

            <div className="mt-8">

                <h3 className="font-bold text-orange-600 mb-3">
                    📈 Resume Improvements
                </h3>

                {match.resume_improvements?.length ? (

                    <ul className="list-disc ml-5 space-y-2">

                        {match.resume_improvements.map((item, index) => (

                            <li key={index}>{item}</li>

                        ))}

                    </ul>

                ) : (

                    <p className="text-gray-500 italic">
                        No suggestions.
                    </p>

                )}

            </div>

            <div className="mt-8 p-5 bg-blue-50 rounded-xl">

                <h3 className="font-bold text-blue-700 mb-2">
                    ⭐ Final Recommendation
                </h3>

                <p>

                    {match.final_recommendation || "No recommendation available."}

                </p>

            </div>

        </Card>

    );

}

export default JobMatchCard;