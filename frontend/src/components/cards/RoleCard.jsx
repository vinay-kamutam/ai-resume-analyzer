import Card from "./Card";

function RoleCard({ role }) {

    return (

        <Card
            title="Recommended Role"
            icon="🎯"
        >

            <h3 className="text-2xl font-semibold text-blue-600">

                {role}

            </h3>

        </Card>

    );

}

export default RoleCard;